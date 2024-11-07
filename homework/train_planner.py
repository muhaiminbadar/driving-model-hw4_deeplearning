"""
Usage:
    python3 -m homework.train_planner --your_args here
"""

print("Time to train")

# train(
#    model_name="linear_planner",
#    transform_pipeline="state_only",
#    num_workers=4,
#    lr=1e-4,
#    batch_size=128,
#    num_epoch=40,
#)

def train(
    model_name: str,
    transform_pipeline: str,
    num_workers: int,
    lr: float,
    batch_size: int,
    num_epoch: int,
):
    print(f"Training {model_name} with {transform_pipeline} pipeline")
    print(f"Using {num_workers} workers")
    print(f"Learning rate: {lr}")
    print(f"Batch size: {batch_size}")
    print(f"Number of epochs: {num_epoch}")
    print("Training completed")
    return None