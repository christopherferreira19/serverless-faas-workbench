#! /bin/bash

shopt -s nullglob

DIR="$(readlink -f "$(dirname "$0")")"
DATASET_ROOT=${DIR}/../../dataset/

MC=${MC:-mc}
SERVER=minio

prepare_bucket() {
	local bucket=$1; shift
	local path=$1; shift

	$MC mb -p $SERVER/"$bucket"
	for file in "$path"/*; do
		$MC cp "$file" $SERVER/"$bucket/$(basename "$file")"
	done
}

prepare_bucket "image"  "$DATASET_ROOT/image"
$MC mb -p $SERVER/imageoutput
prepare_bucket "model"  "$DATASET_ROOT/model"
prepare_bucket "review" "$DATASET_ROOT/amzn_fine_food_reviews"
