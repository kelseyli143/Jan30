from new_temp_conv_script import convert_c_to_f


def test_convert_c_to_f():
	answer = convert_c_to_f(20.0)
	expected = 68.0
	assert answer == expected


def test_2():
        answer = convert_c_to_f(-40)
        expected = -40
        assert answer == expected


def test_3():
	answer = convert_c_to_f(50)
	expected = 122
        assert answer == expected


def test_fever_detection_bad():
	temp_list = [93.0, 98.0, 100.0, 105.0, 101.1]
	max_temp, is_fever = fever_detection(temp_list)
	expected_max = 105.0
	is_fever = True
	expected_fever = True

	assert max_temp == expected_max
	assert is_fever == expected_fever

# multiple assertions is not the best idea because you have to make sure it catches
# both assertions
