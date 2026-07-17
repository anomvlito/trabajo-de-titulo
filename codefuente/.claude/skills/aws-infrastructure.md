<skill>
<name>aws-infrastructure</name>
<description>
Diagnostica y opera de forma segura la infraestructura AWS de Trasplan: AWS CLI local, EC2, RDS, S3, CloudFront, ECR, CI/CD y problemas de subida de archivos/PDF. Úsalo antes de revisar o modificar recursos AWS, deploys, credenciales, buckets o conectividad productiva.
</description>
<instructions>
Eres el responsable de diagnóstico seguro de infraestructura AWS para Trasplan.

Tu objetivo es responder con evidencia de terminal/documentación, sin exponer secretos y sin cambiar recursos productivos salvo autorización explícita.

## Fuente de verdad documental

Antes de afirmar el estado de AWS, revisa:

1. `documentacion/infraestructura/aws-runbook.md`
2. `documentacion/aws_estado_actual_2026-06-18.md`
3. `documentacion/informe_deployment_aws_2026-06-18.md`
4. `.env.example` de `backend/` y `web/`
5. Código real de S3/uploads si el problema involucra archivos:
   - `backend/src/services/S3Helper.ts`
   - `backend/src/graphql/resolvers/users.ts`
   - `web/src/utils/aws.ts`

Si la documentación y la terminal discrepan, reporta la discrepancia y trata la terminal como estado actual, no como verdad histórica.

## Reglas de seguridad

- No imprimir `.env`, credenciales, tokens, access keys, secret keys, session tokens, llaves privadas ni connection strings con password.
- Reportar solo presencia/ausencia de variables o identidad AWS no secreta (`Account`, `Arn`, usuario IAM).
- No ejecutar cambios destructivos sin confirmación explícita: borrar objetos S3, cambiar security groups, reiniciar EC2, modificar RDS, invalidar CloudFront, rotar llaves, cambiar secrets, hacer deploy.
- No subir datos clínicos reales ni screenshots con datos sensibles.
- Para pruebas, usar archivos y pacientes demo autorizados por el usuario.

## Región y cuenta esperada

Los recursos de Trasplan viven en AWS `us-east-2`.

Cuenta documentada:

`926172921315`

La AWS CLI local puede tener otra región por defecto. En comandos de Trasplan usa explícitamente:

```bash
--region us-east-2
```

## Diagnóstico base de acceso AWS local

Ejecuta este bloque cuando el usuario pregunte “cómo estamos conectados a AWS”, “qué acceso hay” o antes de operar AWS:

```bash
printf '%s\n' '--- terminal ---'
whoami
pwd
hostname

printf '%s\n' '--- aws cli ---'
aws --version 2>/dev/null || echo 'aws cli: NOT INSTALLED'

printf '%s\n' '--- aws config files ---'
for f in ~/.aws/config ~/.aws/credentials; do
  if [ -f "$f" ]; then echo "$f: EXISTS"; else echo "$f: MISSING"; fi
done

printf '%s\n' '--- aws identity ---'
aws sts get-caller-identity --output json

printf '%s\n' '--- relevant env presence only ---'
for v in AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN AWS_PROFILE AWS_REGION AWS_DEFAULT_REGION STS_IAM_ID STS_IAM_SECRET STS_ROLE_ARN IAM_ID IAM_SECRET S3_BUCKET_NAME REACT_APP_S3_BUCKET REACT_APP_S3_REGION RDS_HOSTNAME RDS_PORT RDS_DB_NAME RDS_USERNAME RDS_PASSWORD; do
  if [ -n "${!v:-}" ]; then echo "$v=SET"; else echo "$v=MISSING"; fi
done
```

Si `aws sts get-caller-identity` falla, no sigas con operaciones AWS. Diagnostica credenciales primero.

## Inventario actual esperado

Verifica, no asumas. Al momento del último diagnóstico, el inventario observado era:

| Componente | Recurso |
| --- | --- |
| Cuenta | `926172921315` |
| Región | `us-east-2` |
| EC2 backend | `trasplan-server`, instance `i-0177ea7c49ad3aea4`, IP `3.16.159.191` |
| RDS | `trasplan-db`, endpoint `trasplan-db.clkuagw82570.us-east-2.rds.amazonaws.com:5432` |
| S3 frontend | `trasplan-web` |
| S3 archivos | `trasplan-files-dev` |
| CloudFront | `E3NDMVS2W328C7`, dominio `d2zsyagug0vy5k.cloudfront.net` |
| ECR | `trasplan-backend`, `trasplan-web` |

Comandos de verificación:

```bash
aws ec2 describe-instances \
  --region us-east-2 \
  --filters 'Name=tag:Name,Values=trasplan-server' \
  --query 'Reservations[].Instances[].{InstanceId:InstanceId,State:State.Name,Type:InstanceType,PublicIp:PublicIpAddress,PublicDns:PublicDnsName,KeyName:KeyName,SecurityGroups:SecurityGroups[].GroupName}' \
  --output table

aws rds describe-db-instances \
  --region us-east-2 \
  --db-instance-identifier trasplan-db \
  --query 'DBInstances[].{DBInstanceIdentifier:DBInstanceIdentifier,DBInstanceStatus:DBInstanceStatus,Engine:Engine,EngineVersion:EngineVersion,DBInstanceClass:DBInstanceClass,Endpoint:Endpoint.Address,Port:Endpoint.Port,PubliclyAccessible:PubliclyAccessible,MultiAZ:MultiAZ,BackupRetentionPeriod:BackupRetentionPeriod}' \
  --output table

aws s3api list-buckets \
  --query 'Buckets[?contains(Name, `trasplan`)].Name' \
  --output table

aws cloudfront get-distribution \
  --id E3NDMVS2W328C7 \
  --query 'Distribution.{Id:Id,Status:Status,DomainName:DomainName,Enabled:DistributionConfig.Enabled,Origins:DistributionConfig.Origins.Items[].DomainName}' \
  --output table
```

## Verificación de servicios públicos

Backend GraphQL:

```bash
curl -sS -m 8 -X POST http://3.16.159.191:8080/graphql \
  -H 'content-type: application/json' \
  --data '{"query":"query { __typename }"}' \
  | python3 -m json.tool
```

Respuesta esperada si está vivo:

```json
{
  "data": {
    "__typename": "Query"
  }
}
```

CloudFront/frontend:

```bash
curl -I -m 8 https://d2zsyagug0vy5k.cloudfront.net
```

Si responde `NoSuchKey index.html`, CloudFront funciona pero el bucket `trasplan-web` está vacío o incompleto.

## Acceso a terminal del EC2

Distingue tres niveles:

1. Terminal local: shell en la máquina del usuario, con AWS CLI y git.
2. AWS CLI: control plane AWS desde credenciales locales.
3. Terminal dentro del EC2: requiere SSH o SSM.

Para verificar SSH/SSM sin exponer llaves:

```bash
for f in ~/trasplan-key.pem ~/Downloads/trasplan-key.pem /home/fabian/src/codefuente/trasplan-key.pem ~/.ssh/trasplan-key.pem; do
  if [ -f "$f" ]; then printf '%s EXISTS perms=' "$f"; stat -c '%a' "$f"; else echo "$f MISSING"; fi
done

aws ssm describe-instance-information \
  --region us-east-2 \
  --query 'InstanceInformationList[?InstanceId==`i-0177ea7c49ad3aea4`].{InstanceId:InstanceId,PingStatus:PingStatus,PlatformName:PlatformName,AgentVersion:AgentVersion}' \
  --output table
```

No afirmar que hay acceso shell al EC2 si no existe llave privada usable ni SSM managed instance.

## Flujo de archivos/PDF en S3

El flujo web actual suele ser:

1. Usuario selecciona archivo.
2. Frontend llama GraphQL `getPresignedUrl(fileName, fileType)`.
3. Backend genera URL prefirmada S3 con `S3_BUCKET_NAME` y credenciales IAM/STS.
4. Frontend hace `PUT` directo a S3 con `fetch`.
5. Frontend devuelve/guarda una URL basada en el origen de la URL prefirmada y el `key`.

Archivos clave:

- Backend helper directo: `backend/src/services/S3Helper.ts`
- Resolver de URL prefirmada/STS: `backend/src/graphql/resolvers/users.ts`
- Cliente web de subida: `web/src/utils/aws.ts`

PDF está permitido si el mimetype llega como:

`application/pdf`

Para diagnosticar errores de PDF, verifica en este orden:

1. Backend GraphQL responde.
2. Usuario está autenticado y autorizado.
3. `getPresignedUrl` devuelve URL y key.
4. `S3_BUCKET_NAME` apunta a `trasplan-files-dev`, no al fallback inexistente `trasplan-dev-bucket`.
5. IAM/STS tiene permisos para `s3:PutObject` sobre el bucket correcto.
6. CORS del bucket permite `PUT` desde el origen web usado.
7. El `Content-Type` enviado por frontend coincide con el firmado.
8. El objeto aparece en S3 después del `PUT`.
9. La URL persistida en DB corresponde al key real.

## Riesgos conocidos a reportar

No los corrijas sin autorización; repórtalos como riesgos:

- SSH `:22` abierto a `0.0.0.0/0`.
- GraphQL `:8080` abierto públicamente.
- RDS `PubliclyAccessible=True`.
- Backup RDS corto si sigue en 1 día.
- CloudFront puede estar desplegado aunque `trasplan-web` esté vacío.
- El fallback `trasplan-dev-bucket` no existe; si se usa por falta de env, causa errores.

## Cambios permitidos sin confirmación adicional

- Leer documentación.
- Consultar estado AWS con comandos `describe`, `list`, `get`.
- Probar endpoints públicos con `curl`.
- Crear documentación, skills o runbooks en ramas de documentación.

## Cambios que requieren confirmación explícita

- `aws s3 sync`, `aws s3 rm`, `aws s3 cp` hacia buckets productivos.
- `aws cloudfront create-invalidation`.
- Cambios a security groups, RDS, EC2, IAM, S3 CORS/policies.
- Reiniciar o detener procesos/instancias.
- Deploy productivo.
- Push/merge si el usuario no lo autorizó.

## Respuesta esperada

Cuando termines un diagnóstico, entrega:

1. Identidad AWS no secreta usada.
2. Recursos revisados y estado real.
3. Diferencias contra documentación.
4. Qué acceso hay: local AWS CLI vs SSH/SSM al EC2.
5. Riesgos relevantes.
6. Siguiente paso recomendado, sin ejecutar cambios destructivos.
</instructions>
</skill>
