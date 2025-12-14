# Dockerfile für PostgreSQL
FROM postgres:latest

# Setze Standard-Umgebungsvariablen (kann beim Start überschrieben werden)
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=MeinStarkesPasswort
ENV POSTGRES_DB=mydatabase

# Optional: SQL-Dateien ins Image kopieren, z.B. für Schema oder Initialdaten
# COPY ./init.sql /docker-entrypoint-initdb.d/
