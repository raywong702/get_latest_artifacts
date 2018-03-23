```bash
# Build test image
docker build . -t test

# Run test nginx
docker run -d -p 8080:8080 --rm --name test test

# Stop test nginx
docker stop test
```

.