## Docker Compose Setup for Web Application with PostgreSQL

This document explains how to use the provided Docker Compose file to run a web application connected to a PostgreSQL database.

**Prerequisites:**

* Docker and Docker Compose installed on your system.

**Database Version:**

This setup uses PostgreSQL version **13**.

**Environment Variables:**

* **POSTGRES_DB:** Name of the database (default: `postgres`).
* **POSTGRES_USER:** Username for the database (default: `username`).
* **POSTGRES_PASSWORD:** Password for the database (default: `1234`).
* **DB_HOST:** Hostname of the database (default: `localhost`, which resolves to the container name).
* **DB_PORT:** Port number of the database (default: `5432`).
* **DB_NAME:** Name of the database (default: `postgres`).
* **DB_USER:** Username for the database (default: `username`).
* **DB_PASSWORD:** Password for the database (default: `1234`).

**How to Use:**

1. **Update Environment Variables:**

   Modify the `environment` sections in the `postgres` and `web` services to match your desired database credentials and application settings.

2. **Build and Start the Containers:**

   Open a terminal in the directory containing the `docker-compose.yml` file and run the following command:

   ```bash
   docker-compose up --build -d
   ```

   This will:

   * Build the `web` service image from the `Dockerfile` in the current directory.
   * Start both the `postgres` and `web` containers in detached mode.

3. **Access the Web Application:**

   Once the containers are running, you can access your web application in your browser at `http://localhost:8000`.

4. **Connect to the PostgreSQL Database:**

   You can connect to the PostgreSQL database using any PostgreSQL client (e.g., psql) by providing the following connection details:

   * **Host:** `localhost`
   * **Port:** `5432`
   * **Database:** `postgres`
   * **Username:** `username`
   * **Password:** `1234`

   so settings.py MUST be:DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "username",
        "PASSWORD": "1234",
        "HOST": "postgres",
        "PORT": "5432",
    }
}
(NOTE: if get err:exec /scripts/entrypoint.sh: no such file or directory you can fix by:chmod +x entrypoint.sh or Go to Edit > EOL Conversion > Unix (LF))