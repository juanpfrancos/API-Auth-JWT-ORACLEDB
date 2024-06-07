from fastapi import APIRouter, Depends, HTTPException
from models.user import UserSignUp
from routes.login import get_current_user

protected_router = APIRouter(tags=['Protected'])

# Este endpoint solo será accesible si se proporciona un token válido
@protected_router.get("/protected")
def get_protected(current_user: UserSignUp = Depends(get_current_user)):
    return {"message": f"Bienvenido {current_user.FIRST_NAME} {current_user.FIRST_NAME}"}

# Endpoint para obtener información del usuario autenticado
@protected_router.get("/user")
def get_user(current_user: UserSignUp = Depends(get_current_user)):
    return current_user

# Endpoint para actualizar información del usuario autenticado
@protected_router.put("/user")
def update_user(updated_user: UserSignUp, current_user: UserSignUp = Depends(get_current_user)):
    # Aquí puedes implementar la lógica para actualizar la información del usuario en la base de datos
    return {"message": "Información actualizada correctamente"}