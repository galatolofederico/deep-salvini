#!/bin/sh

base_model="LorenzoDeMattei/GePpeTto"
dataset="./datasets/salvini.txt"
name=$(date +%s)
output_dir="./models/$name/"
logging_dir="./runs/$name"
epochs="2"

python run_language_modeling.py \
    --output_dir="$output_dir" \
    --model_type=gpt2 \
    --model_name_or_path="$base_model" \
    --num_train_epochs="$epochs" \
    --overwrite_output_dir \
    --do_train \
    --logging_dir="$logging_dir" \
    --logging_steps=2 \
    --train_data_file="$dataset" \
    --per_gpu_train_batch_size=8 \
    --block_size=128 \
    --save_steps=10000