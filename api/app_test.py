from app import process_query, get_list_of_number, largest, square_cube


# def test_knows_about_dinosaurs():
#     assert process_query("dinosaurs") == "Dinosaurs ruled the Earth \
# 200 million years ago"
#
#
# def test_does_not_know_about_asteroids():
#     assert process_query("asteroids") == "Unknown"
#
#
# def test_does_not_know_about_asteroids():
#     assert process_query("asteroids") == "Unknown"


def test_knows_team_name():
    assert process_query('What is your name?') == 'Lisa_Jamie'


def test_get_list_of_number():
    query = 'What is 22 plus 20?'
    assert get_list_of_number(query) == [22, 20]
    query = 'Which of the following numbers is the largest: 73, 82, 15?'
    assert get_list_of_number(query) == [73, 82, 15]


def test_square_cube():

    []
    assert square_cube()



# def test_largest():
#     nums = [20, 40]
#     a