import pytest

# Se ejecutan los tests
pytest.main(["-s","tests/test_get.py"])   # Alta de usuario
pytest.main(["-s","tests/test_post.py"])  # Validación del alta de usuario
pytest.main(["-s","tests/test_put.py"])   # Modificación de datos del usuario
pytest.main(["-s","tests/test_get2.py"])  # Validación de los cambios efectuados
