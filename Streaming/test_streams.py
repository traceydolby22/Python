import pytest

from streams import streams, get_completed_streams, group_by_platform, get_longest_stream, get_average_rating_by_platform, get_stream_summary

def test_completed_streams():
    result = get_completed_streams(streams)
    assert "The Mandalorian" in result
    assert "The Bear" in result
    assert "Dopesick" in result
    assert "Loki" in result
    assert "Andor" not in result

def test_group_by_platform():
    result = group_by_platform(streams)
    assert "The Mandalorian" in result["Disney+"]
    assert "Andor" in result["Disney+"]
    assert "Loki" in result["Disney+"]
    assert "Ms. Marvel" in result["Disney+"]
    assert "Obi-Wan Kenobi" in result["Disney+"]
    assert "Only Murders in the Building" in result["Hulu"]
    assert "The Bear" in result["Hulu"]
    assert "Abbott Elementary" in result["Hulu"]
    assert "Dopesick" in result["Hulu"]
    assert "Little Fires Everywhere" in result["Hulu"]

def test_get_longest_stream():
    result = get_longest_stream(streams)
    assert "Dopesick" in result
    assert "The Mandalorian" not in result

def test_get_average_rating_by_platform():
    result = get_average_rating_by_platform(streams)
    assert result["Disney+"] == 4.56
    assert result["Hulu"] == 4.6

def test_get_stream_summary():
    result = get_stream_summary(streams) 
    assert "The Mandalorian (Disney+): 45 min" in result
    assert "Only Murders in the Building (Hulu): 32 min" in result
    assert "Ms. Marvel (Disney+): 40 min" not in result
