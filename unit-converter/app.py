import streamlit as st

def length_converter():
    st.subheader("Length Converter")
    length_options = ["Meter to Kilometer", "Kilometer to Meter", "Meter to Centimeter", "Centimeter to Meter"]
    length_choice = st.selectbox("Choose conversion", length_options)

    if length_choice == "Meter to Kilometer":
        meter = st.number_input("Enter length in meters")
        kilometer = meter / 1000
        st.write(f"{meter} meters is equal to {kilometer} kilometers")

    elif length_choice == "Kilometer to Meter":
        kilometer = st.number_input("Enter length in kilometers")
        meter = kilometer * 1000
        st.write(f"{kilometer} kilometers is equal to {meter} meters")

    elif length_choice == "Meter to Centimeter":
        meter = st.number_input("Enter length in meters")
        centimeter = meter * 100
        st.write(f"{meter} meters is equal to {centimeter} centimeters")

    elif length_choice == "Centimeter to Meter":
        centimeter = st.number_input("Enter length in centimeters")
        meter = centimeter / 100
        st.write(f"{centimeter} centimeters is equal to {meter} meters")


def mass_converter():
    st.subheader("Mass Converter")
    mass_options = ["Kilogram to Gram", "Gram to Kilogram", "Kilogram to Milligram", "Milligram to Kilogram"]
    mass_choice = st.selectbox("Choose conversion", mass_options)

    if mass_choice == "Kilogram to Gram":
        kilogram = st.number_input("Enter mass in kilograms")
        gram = kilogram * 1000
        st.write(f"{kilogram} kilograms is equal to {gram} grams")

    elif mass_choice == "Gram to Kilogram":
        gram = st.number_input("Enter mass in grams")
        kilogram = gram / 1000
        st.write(f"{gram} grams is equal to {kilogram} kilograms")

    elif mass_choice == "Kilogram to Milligram":
        kilogram = st.number_input("Enter mass in kilograms")
        milligram = kilogram * 1e6
        st.write(f"{kilogram} kilograms is equal to {milligram} milligrams")

    elif mass_choice == "Milligram to Kilogram":
        milligram = st.number_input("Enter mass in milligrams")
        kilogram = milligram / 1e6
        st.write(f"{milligram} milligrams is equal to {kilogram} kilograms")


def temperature_converter():
    st.subheader("Temperature Converter")
    temp_options = ["Celsius to Fahrenheit", "Fahrenheit to Celsius"]
    temp_choice = st.selectbox("Choose conversion", temp_options)

    if temp_choice == "Celsius to Fahrenheit":
        celsius = st.number_input("Enter temperature in Celsius")
        fahrenheit = (celsius * 9/5) + 32
        st.write(f"{celsius}°C is equal to {fahrenheit}°F")

    elif temp_choice == "Fahrenheit to Celsius":
        fahrenheit = st.number_input("Enter temperature in Fahrenheit")
        celsius = (fahrenheit - 32) * 5/9
        st.write(f"{fahrenheit}°F is equal to {celsius}°C")


def main():
    st.title("Unit Converter App")
    converter_options = ["Length", "Mass", "Temperature"]
    converter_choice = st.selectbox("Choose converter type", converter_options)

    if converter_choice == "Length":
        length_converter()
    elif converter_choice == "Mass":
        mass_converter()
    elif converter_choice == "Temperature":
        temperature_converter()


if __name__ == "__main__":
    main()