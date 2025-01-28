# Running PostgreSQL Locally

To run PostgreSQL locally using Docker, follow these steps:

1. Start the Docker containers:

   ```bash
   docker compose up
   ```

2. Check the running containers:

   ```bash
   docker ps
   ```

3. Access the PostgreSQL container:

   ```bash
   docker exec -it <container_id> bash
   ```

4. Connect to the PostgreSQL database:

   ```bash
   psql -U postgres -d MineBoxDB
   ```

Replace `<container_id>` with the actual container ID from the `docker ps` output.

**Alternatively, you can use Adminer to manage your database:**

1. Open your browser and go to [http://localhost:8080](http://localhost:8080).

2. Enter the following details to log in:
   - **System**: PostgreSQL
   - **Server**: MineBox
   - **Username**: postgres
   - **Password**: postgres
   - **Database**: MineBoxDB

## Author

[Aryan Khurana](https://github.com/AryanK1511)
