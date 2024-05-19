import gamepad_stream_controller

if __name__ == "__main__":
    gamepad_stream_controller.run_event_loop(
        gamepad_stream_controller.print_add,
        gamepad_stream_controller.print_remove,
        gamepad_stream_controller.key_received
    )
