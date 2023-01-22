path=$(realpath $1)
echo $path
docker run --rm -v $path:/application/islands.txt island-counter islands.txt
