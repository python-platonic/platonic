from platonic.queue import MessageReceiveTimeout, MessageTooLarge


def test_message_receive_timeout_one_second():
    """One second."""
    assert str(MessageReceiveTimeout(
        queue='mock',  # type: ignore
        timeout=1,
    )) == (
        'No messages received within 1 second.\n'
        '\n  Queue: mock'
    )


def test_message_receive_timeout_two_seconds():
    """Two seconds."""
    assert str(MessageReceiveTimeout(
        queue='mock',  # type: ignore
        timeout=2,
    )) == (
        'No messages received within 2 seconds.\n'
        '\n  Queue: mock'
    )


def test_message_too_large():
    """Message too large."""
    exception = MessageTooLarge(
        max_supported_size=8,
        message_body='abyr abyr abyr valg',
        message_preview_size=4,
    )

    assert str(exception) == (
        'Message is too large.\n'
        '\n'
        'Provided message size is 19 bytes, while\n'
        'maximum message size is 8 bytes.\n'
        '\n'
        'Message preview:\n'
        '    abyr...valg'
    )
