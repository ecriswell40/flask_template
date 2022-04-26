from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/estimate')
def estimate():
   # def calculate_tank_top(tank_top):
       # tank_top= 3.14*(tankradius)

    #def calculate_tank_sides(tank_sides):
       # tank_sides=2(3.14([tankradius]*[tankheight]))

   # def calculate_total_area_in(total_area_in):
      #  tank_area_in=tank_top + tank_sides

   # def calculate_total_sqft(total_sqft):
       # total_sqft=total_area_in/144

   # def calculate_material_cost(material_cost):
      #  material_cost=total_sqft*25

   # def calculate_labor_cost(labor_cost):
      #  labor_cost=total_sqft*15

   # def calculate_total_cost(total_cost):
      #  total_cost=material_cost + labor_cost
      #  return (Estimated total cost would be (total_cost))
    return render_template('estimate.html')

if __name__ == '__main__':
    app.run(debug=True)