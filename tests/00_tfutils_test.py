from singexample import tf_utils


def test_tb_logdir():
    """Test logdir generation."""
    logdir_base = tf_utils.get_tb_logdir("hello", False)
    assert str(logdir_base).split("/")[-3:] == ["output", "logs", "hello"]

    logdir_time = tf_utils.get_tb_logdir("hello")
    assert str(logdir_time).split("/")[-4:-1] == ["output", "logs", "hello"]
    assert len(str(logdir_time).split("/")[-1]) == 17, "Datetime output consistency"
