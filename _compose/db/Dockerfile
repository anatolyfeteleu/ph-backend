FROM postgres:bullseye
RUN localedef -i ru_RU -c -f UTF-8 -A /usr/share/locale/locale.alias ru_RU.UTF-8
ENV LANG ru_RU.utf8

# Copy in the load-extensions script
COPY ./_compose/scripts/install-db-extensions /docker-entrypoint-initdb.d/install-db-extensions.sh
