SHELL := /bin/bash

ROOT_DIR := $(CURDIR)
BACKEND_DIR := $(ROOT_DIR)/backend
WEB_DIR := $(ROOT_DIR)/web
RUN_DIR := $(ROOT_DIR)/.make
PID_DIR := $(RUN_DIR)/pids
LOG_DIR := $(RUN_DIR)/logs

BACKEND_PORT ?= 8080
WEB_PORT ?= 3000

DB_NAME ?= backend_grupo_2
DB_USER ?= iic2154
DB_PASSWORD ?= iic2154
DB_HOST ?= localhost
DB_PORT ?= 5432
DB_MODE ?= local

BACKEND_ENV := SECRET=$${SECRET:-trasplan} \
	BASIC_USER_PASSWORD=$${BASIC_USER_PASSWORD:-123456} \
	RDS_HOSTNAME=$${RDS_HOSTNAME:-$(DB_HOST)} \
	RDS_PORT=$${RDS_PORT:-$(DB_PORT)} \
	RDS_DB_NAME=$${RDS_DB_NAME:-$(DB_NAME)} \
	RDS_USERNAME=$${RDS_USERNAME:-$(DB_USER)} \
	RDS_PASSWORD=$${RDS_PASSWORD:-$(DB_PASSWORD)}

WEB_ENV := BROWSER=none HOST=0.0.0.0 PORT=$(WEB_PORT) \
	WATCHPACK_POLLING=true CHOKIDAR_USEPOLLING=true CHOKIDAR_INTERVAL=1000 \
	REACT_APP_API_URL=$${REACT_APP_API_URL:-http://localhost:$(BACKEND_PORT)/graphql}

.DEFAULT_GOAL := help
.PHONY: help run kill reset db db-local db-docker reset-local reset-docker migrate seed seed-if-empty deps status wait ready logs logs-backend logs-web

help:
	@printf '%s\n' \
		'Trasplan local' \
		'' \
		'Targets principales:' \
		'  make run          Asegura PostgreSQL local, migra, seed si falta, backend y web' \
		'  make kill         Detiene backend/web y libera puertos 3000/8080' \
		'  make reset        Resetea DB local y levanta todo desde cero' \
		'' \
		'Targets utiles:' \
		'  make db           Asegura solo la base de datos local' \
		'  make migrate      Ejecuta migraciones backend' \
		'  make seed         Ejecuta seeders backend aunque existan datos' \
		'  make status       Muestra procesos, puertos y rutas de logs' \
		'  make logs         Sigue logs backend y web' \
		'  make ready        Espera/verifica que web y backend respondan' \
		'' \
		'Variables utiles:' \
		'  DB_MODE=local|docker  local usa PostgreSQL del sistema; docker usa backend/docker-compose.yml' \
		'  DB_USER=iic2154 DB_PASSWORD=iic2154 DB_NAME=backend_grupo_2' \
		'' \
		'Puertos por defecto: web 3000, backend 8080, postgres 5432'

run: kill db migrate seed-if-empty
	@mkdir -p "$(PID_DIR)" "$(LOG_DIR)"
	@printf 'Levantando backend en http://localhost:%s/graphql\n' "$(BACKEND_PORT)"
	@cd "$(BACKEND_DIR)" && nohup env $(BACKEND_ENV) npx ts-node src/index.ts < /dev/null >"$(LOG_DIR)/backend.log" 2>&1 & echo $$! >"$(PID_DIR)/backend.pid"
	@printf 'Levantando web en http://localhost:%s\n' "$(WEB_PORT)"
	@cd "$(WEB_DIR)" && nohup env $(WEB_ENV) npm start < /dev/null >"$(LOG_DIR)/web.log" 2>&1 & echo $$! >"$(PID_DIR)/web.pid"
	@$(MAKE) --no-print-directory wait
	@$(MAKE) --no-print-directory status
	@printf '\nMostrando logs en tiempo real (Ctrl+C para salir)...\n'
	@$(MAKE) --no-print-directory logs

kill:
	@mkdir -p "$(PID_DIR)" "$(LOG_DIR)"
	@for name in backend web; do \
		pid_file="$(PID_DIR)/$$name.pid"; \
		if [ -f "$$pid_file" ]; then \
			pid="$$(cat "$$pid_file")"; \
			if kill -0 "$$pid" >/dev/null 2>&1; then \
				printf 'Deteniendo %s pid %s\n' "$$name" "$$pid"; \
				kill "$$pid" >/dev/null 2>&1 || true; \
			fi; \
			rm -f "$$pid_file"; \
		fi; \
	done
	@for port in "$(WEB_PORT)" "$(BACKEND_PORT)"; do \
		if command -v lsof >/dev/null 2>&1; then \
			pids="$$(lsof -ti tcp:$$port 2>/dev/null || true)"; \
			if [ -n "$$pids" ]; then \
				printf 'Liberando puerto %s: %s\n' "$$port" "$$pids"; \
				kill $$pids >/dev/null 2>&1 || true; \
			fi; \
		elif command -v fuser >/dev/null 2>&1; then \
			fuser -k "$$port/tcp" >/dev/null 2>&1 || true; \
		fi; \
	done
	@sleep 1

db:
	@if [ "$(DB_MODE)" = "docker" ]; then \
		$(MAKE) --no-print-directory db-docker; \
	else \
		$(MAKE) --no-print-directory db-local; \
	fi

db-local:
	@printf 'Asegurando PostgreSQL local en %s:%s...\n' "$(DB_HOST)" "$(DB_PORT)"
	@if ! pg_isready -h "$(DB_HOST)" -p "$(DB_PORT)" >/dev/null 2>&1; then \
		printf 'PostgreSQL no responde. Intentando iniciar servicio local...\n'; \
		if command -v systemctl >/dev/null 2>&1; then \
			sudo systemctl start postgresql || true; \
		elif command -v service >/dev/null 2>&1; then \
			sudo service postgresql start || true; \
		fi; \
	fi
	@for attempt in $$(seq 1 30); do \
		if pg_isready -h "$(DB_HOST)" -p "$(DB_PORT)" >/dev/null 2>&1; then \
			printf 'PostgreSQL listo.\n'; \
			break; \
		fi; \
		if [ "$$attempt" = "30" ]; then \
			printf 'PostgreSQL no quedo listo. Ejecuta: sudo systemctl start postgresql\n'; \
			exit 1; \
		fi; \
		sleep 1; \
	done
	@if ! PGPASSWORD="$(DB_PASSWORD)" psql -h "$(DB_HOST)" -p "$(DB_PORT)" -U "$(DB_USER)" -d postgres -tAc 'select 1' >/dev/null 2>&1; then \
		printf 'Creando/asegurando usuario local %s...\n' "$(DB_USER)"; \
		sudo -u postgres psql -tc "select 1 from pg_roles where rolname='$(DB_USER)'" | grep -q 1 || sudo -u postgres createuser "$(DB_USER)" --createdb --superuser; \
		sudo -u postgres psql -c "alter user $(DB_USER) with password '$(DB_PASSWORD)';"; \
	fi
	@for db in "$(DB_NAME)" "$(DB_NAME)_test"; do \
		if ! PGPASSWORD="$(DB_PASSWORD)" psql -h "$(DB_HOST)" -p "$(DB_PORT)" -U "$(DB_USER)" -d postgres -tAc "select 1 from pg_database where datname='$$db'" | grep -q 1; then \
			printf 'Creando base local %s...\n' "$$db"; \
			PGPASSWORD="$(DB_PASSWORD)" createdb -h "$(DB_HOST)" -p "$(DB_PORT)" -U "$(DB_USER)" "$$db"; \
		fi; \
	done

db-docker:
	@printf 'Levantando Postgres Docker desde backend/docker-compose.yml...\n'
	@cd "$(BACKEND_DIR)" && docker compose up -d database || docker-compose up -d database
	@printf 'Esperando PostgreSQL Docker'
	@for attempt in $$(seq 1 30); do \
		if cd "$(BACKEND_DIR)" && docker compose exec -T database pg_isready -U "$(DB_USER)" -d "$(DB_NAME)" >/dev/null 2>&1; then \
			printf '\nPostgreSQL Docker listo.\n'; \
			exit 0; \
		fi; \
		printf '.'; sleep 1; \
	done; \
	printf '\nPostgreSQL Docker no quedo listo.\n'; exit 1

reset: kill
	@if [ "$(DB_MODE)" = "docker" ]; then \
		$(MAKE) --no-print-directory reset-docker; \
	else \
		$(MAKE) --no-print-directory reset-local; \
	fi
	@$(MAKE) --no-print-directory run

reset-local:
	@$(MAKE) --no-print-directory db-local
	@printf 'Reseteando bases locales %s y %s_test...\n' "$(DB_NAME)" "$(DB_NAME)"
	@PGPASSWORD="$(DB_PASSWORD)" dropdb -h "$(DB_HOST)" -p "$(DB_PORT)" -U "$(DB_USER)" --if-exists "$(DB_NAME)"
	@PGPASSWORD="$(DB_PASSWORD)" dropdb -h "$(DB_HOST)" -p "$(DB_PORT)" -U "$(DB_USER)" --if-exists "$(DB_NAME)_test"
	@PGPASSWORD="$(DB_PASSWORD)" createdb -h "$(DB_HOST)" -p "$(DB_PORT)" -U "$(DB_USER)" "$(DB_NAME)"
	@PGPASSWORD="$(DB_PASSWORD)" createdb -h "$(DB_HOST)" -p "$(DB_PORT)" -U "$(DB_USER)" "$(DB_NAME)_test"

reset-docker:
	@printf 'Eliminando contenedores/volumen local de Postgres Docker...\n'
	@cd "$(BACKEND_DIR)" && docker compose down --volumes --remove-orphans || docker-compose down --volumes --remove-orphans

migrate:
	@printf 'Ejecutando migraciones backend...\n'
	@cd "$(BACKEND_DIR)" && env $(BACKEND_ENV) npm run migrate

seed:
	@printf 'Ejecutando seeders backend...\n'
	@cd "$(BACKEND_DIR)" && env $(BACKEND_ENV) npm run seed-db

seed-if-empty:
	@printf 'Verificando seeders backend...\n'
	@if PGPASSWORD="$(DB_PASSWORD)" psql -h "$(DB_HOST)" -p "$(DB_PORT)" -U "$(DB_USER)" -d "$(DB_NAME)" -tAc "select to_regclass('public.users')" | grep -q users; then \
		count="$$(PGPASSWORD="$(DB_PASSWORD)" psql -h "$(DB_HOST)" -p "$(DB_PORT)" -U "$(DB_USER)" -d "$(DB_NAME)" -tAc 'select count(*) from users' 2>/dev/null || echo 0)"; \
	else \
		count=0; \
	fi; \
	if [ "$${count:-0}" = "0" ]; then \
		$(MAKE) --no-print-directory seed; \
	else \
		printf 'Seeders omitidos: users ya tiene %s registro(s).\n' "$$count"; \
	fi

deps:
	@cd "$(BACKEND_DIR)" && npm install --legacy-peer-deps
	@cd "$(WEB_DIR)" && npm install --legacy-peer-deps

wait:
	@printf 'Esperando backend y web'
	@for attempt in $$(seq 1 90); do \
		backend_ok=0; web_ok=0; \
		curl -fsS -X POST "http://localhost:$(BACKEND_PORT)/graphql" -H 'content-type: application/json' --data '{"query":"query { __typename }"}' >/dev/null 2>&1 && backend_ok=1; \
		curl -fsS "http://localhost:$(WEB_PORT)" >/dev/null 2>&1 && web_ok=1; \
		if [ "$$backend_ok" = "1" ] && [ "$$web_ok" = "1" ]; then \
			printf '\nListo: backend http://localhost:%s/graphql, web http://localhost:%s\n' "$(BACKEND_PORT)" "$(WEB_PORT)"; \
			exit 0; \
		fi; \
		printf '.'; sleep 1; \
	done; \
	printf '\nNo quedaron listos a tiempo. Revisa make logs.\n'; exit 1

ready: wait

status:
	@printf '\nEstado local Trasplan\n'
	@printf '  backend log: %s\n' "$(LOG_DIR)/backend.log"
	@printf '  web log:     %s\n' "$(LOG_DIR)/web.log"
	@for entry in "backend:$(BACKEND_PORT)" "web:$(WEB_PORT)"; do \
		name="$${entry%%:*}"; \
		port="$${entry##*:}"; \
		pid_file="$(PID_DIR)/$$name.pid"; \
		if [ -f "$$pid_file" ] && kill -0 "$$(cat "$$pid_file")" >/dev/null 2>&1; then \
			printf '  %s: corriendo pid %s\n' "$$name" "$$(cat "$$pid_file")"; \
		elif command -v lsof >/dev/null 2>&1 && lsof -ti tcp:$$port >/dev/null 2>&1; then \
			printf '  %s: corriendo en puerto %s\n' "$$name" "$$port"; \
		elif ss -ltn 2>/dev/null | grep -Eq "[:.]$$port[[:space:]]"; then \
			printf '  %s: corriendo en puerto %s\n' "$$name" "$$port"; \
		else \
			printf '  %s: detenido\n' "$$name"; \
		fi; \
	done
	@printf '\nPuertos:\n'
	@ss -ltnp 2>/dev/null | grep -E ':$(WEB_PORT)|:$(BACKEND_PORT)|:$(DB_PORT)' || true

logs:
	@tail -f "$(LOG_DIR)/backend.log" "$(LOG_DIR)/web.log"

logs-backend:
	@tail -f "$(LOG_DIR)/backend.log"

logs-web:
	@tail -f "$(LOG_DIR)/web.log"
