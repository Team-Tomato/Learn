class CreateUsers < ActiveRecord::Migration[6.0]
  def change
    create_table :users do |t|
      t.string :name
      t.integer :phone
      t.string :email
      t.string :city
      t.string :state
      t.integer :pin

      t.timestamps
    end
  end
end
