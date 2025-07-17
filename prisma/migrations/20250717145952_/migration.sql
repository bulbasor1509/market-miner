-- CreateEnum
CREATE TYPE "Trade" AS ENUM ('BUY', 'SELL');

-- CreateTable
CREATE TABLE "Bulkdeals" (
    "id" TEXT NOT NULL,
    "date" TIMESTAMP(3) NOT NULL,
    "symbol" TEXT NOT NULL,
    "security_name" TEXT NOT NULL,
    "client_name" TEXT NOT NULL,
    "trade_type" "Trade" NOT NULL,
    "quantity_traded" BIGINT NOT NULL,
    "wt_price" DOUBLE PRECISION NOT NULL,

    CONSTRAINT "Bulkdeals_pkey" PRIMARY KEY ("id")
);
