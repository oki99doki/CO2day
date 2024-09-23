"""redo migration and everything

Revision ID: 418fbc2e0671
Revises: 
Create Date: 2024-09-23 17:59:40.622352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '418fbc2e0671'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('aircrafts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('range', sa.Integer(), nullable=True),
    sa.Column('seats', sa.Integer(), nullable=True),
    sa.Column('gallonsPer100Pass', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('electricityCost', sa.Float(), nullable=True),
    sa.Column('gasCost', sa.Float(), nullable=True),
    sa.Column('gasolineCost', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('make', sa.String(), nullable=True),
    sa.Column('model', sa.String(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('milesPerYear', sa.Float(), nullable=True),
    sa.Column('mpg', sa.Float(), nullable=True),
    sa.Column('co2Produced', sa.Float(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flights',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.String(), nullable=True),
    sa.Column('departure', sa.String(), nullable=True),
    sa.Column('destination', sa.String(), nullable=True),
    sa.Column('international', sa.Boolean(), nullable=True),
    sa.Column('distance', sa.Float(), nullable=True),
    sa.Column('co2Produced', sa.Float(), nullable=True),
    sa.Column('aircraft_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['aircraft_id'], ['aircrafts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('houses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('style', sa.String(), nullable=True),
    sa.Column('size', sa.String(), nullable=True),
    sa.Column('electricityDollars', sa.Float(), nullable=True),
    sa.Column('gasDollars', sa.Float(), nullable=True),
    sa.Column('electricityCo2Produced', sa.Float(), nullable=True),
    sa.Column('gasCo2Produced', sa.Float(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('houses')
    op.drop_table('flights')
    op.drop_table('cars')
    op.drop_table('users')
    op.drop_table('locations')
    op.drop_table('aircrafts')
    # ### end Alembic commands ###
