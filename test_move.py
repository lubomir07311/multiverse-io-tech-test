import pytest
from main import move


def data_provider():
    data = [
		# x, y, direction, gridX, gridY, expected_x, expected_y, is_lost
		[2, 3, "N", 4, 8, 2, 4, False], # successful move North
		[2, 3, "E", 4, 8, 3, 3, False], # successful move East
		[2, 3, "S", 4, 8, 2, 2, False], # successful move East
		[2, 3, "W", 4, 8, 1, 3, False], # successful move East
		[0, 0, "N", 0, 0, 0, 0, True],	# falling off a 0, 0 grid
		[4, 4, "N", 4, 4, 4, 4, True],	# falling off the northern edge
		[4, 4, "E", 4, 4, 4, 4, True],	# falling off the eastern edge
		[4, 0, "S", 4, 4, 4, 0, True],	# falling off the western edge
		[0, 4, "W", 4, 4, 0, 4, True],	# falling off the southern edge
	]
    for row in data:
        yield row
	
	
@pytest.mark.parametrize("test_data", data_provider())
def test_move(test_data):
	x, y, is_lost = move(test_data[0], test_data[1], test_data[2], test_data[3], test_data[4])
	assert x == test_data[5]
	assert y == test_data[6]
	assert is_lost == test_data[7]
