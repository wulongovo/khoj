FROM postgres:16-alpine AS builder
RUN apk add --no-cache build-base postgresql16-dev git
RUN git clone --depth 1 --branch v0.8.0 https://github.com/pgvector/pgvector.git /tmp/pgvector
WORKDIR /tmp/pgvector
RUN make PG_CONFIG=/usr/local/bin/pg_config || true

FROM postgres:16-alpine
COPY --from=builder /tmp/pgvector/vector.so /usr/local/lib/postgresql/
COPY --from=builder /tmp/pgvector/sql/vector.sql /usr/local/share/postgresql/extension/vector--0.8.0.sql
COPY --from=builder /tmp/pgvector/vector.control /usr/local/share/postgresql/extension/
