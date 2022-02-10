import course

def test_Number():
    assert "1411" == course.getNumber("CM241")

def test_ProfessorName():
    assert "Lee" == course.getProfessorName("CM241")

def test_getMeetingTime():
    assert "1:00pm in the afternoon" == course.getMeetingTime("CM241")

