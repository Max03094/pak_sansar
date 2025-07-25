# routers/reports_router.py
from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import pandas as pd
from io import BytesIO
from ..models import AlertStatus
from ..dependencies import get_db_session, role_dependency

reports_router = APIRouter(prefix="/reports", tags=["reports"])

@reports_router.get("/alert-times", response_class=Response)
async def get_alert_times_report(format: str = "csv", db: AsyncSession = Depends(get_db_session), user = Depends(role_dependency(["view_reports"]))):
    result = await db.execute(select(AlertStatus))
    data = [status.__dict__ for status in result.scalars().all()]
    df = pd.DataFrame(data)
    if format == "csv":
        content = df.to_csv(index=False)
        media_type = "text/csv"
    elif format == "excel":
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False)
        content = output.getvalue()
        media_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    else:
        raise HTTPException(400, "Invalid format")
    return Response(content=content, media_type=media_type)