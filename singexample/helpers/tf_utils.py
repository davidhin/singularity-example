import datetime
import os
import socket
import subprocess

import tensorflow as tf

import singexample as se


def start_tensorboard(logdir: str, background: bool = True) -> subprocess.Popen:
    """Start tensorboard.

    Example:
        proc = startTensorboard("output/logs/gpu_test", False)
        proc.terminate()

    Args:
        logdir (str): Directory with log files
        background (bool, optional): Whether to run in background. Defaults to True.

    Returns:
        subprocess.Popen: spawned Tensorboard subprocess
    """
    proc = subprocess.Popen(
        [
            "tensorboard",
            "--logdir",
            logdir,
            "--port",
            "6006",
            "--host",
            socket.gethostname(),
        ]
    )
    if not background:
        proc.wait()
    return proc


def kill_tensorboard_pids() -> None:
    """Find all tensorboard PIDs and kill them."""
    ps = subprocess.Popen(["ps", "x", "-u", os.environ["USER"]], stdout=subprocess.PIPE)
    output = subprocess.check_output(("grep", "-i", "tensorboard"), stdin=ps.stdout)
    output = output.decode().split("\n")
    output = [i.split()[0] for i in output if len(i) > 10]
    subprocess.Popen(["kill"] + output).communicate()


def get_tb_logdir(name: str, inc_time: bool = True) -> str:
    """Get absolute path of log directory for use with TensorBoard.

    Args:
        name (str): Name describing model / configurations
        inc_time (bool): Whether date is appended to end of path. Defaults to True.

    Returns:
        str: Full path to log directory
    """
    log_dir_base = se.get_path(se.outputs_root() / "logs/{}/".format(name))
    if inc_time:
        log_dir_base /= datetime.datetime.now().strftime("%Y_%m_%d-%H%M%S")
    return log_dir_base


def tb_callback(logdir: str) -> tf.keras.callbacks.TensorBoard:
    """Get Tensorboard callback.

    Args:
        logdir (str): Directory for log files.

    Returns:
        tf.keras.callbacks.TensorBoard: Object.
    """
    return tf.keras.callbacks.TensorBoard(log_dir=logdir, histogram_freq=1)
