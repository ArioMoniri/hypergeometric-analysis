import streamlit as st
from scipy.stats import hypergeom

# Title of the web app
st.title("Hypergeometric Test Calculator")

# Descriptions and inputs
st.header("Input Parameters")

# Total number of genes (M)
M = st.number_input("Total number of genes (M):", min_value=1, value=357)
st.write("This represents the total number of items in the population (e.g., total number of genes).")

# Total number of synaptic proteins in the background (n)
n = st.number_input("Total number of synaptic proteins in the background (n):", min_value=1, value=139)
st.write("This is the number of items in the population that are classified as 'successes' (e.g., synaptic proteins).")

# Number of genes in your list (N)
N = st.number_input("Number of genes in your list (N):", min_value=1, value=197)
st.write("This represents the number of items in the sample you are analyzing (e.g., number of genes in your list).")

# Number of synaptic proteins in your list (x)
x = st.number_input("Number of synaptic proteins in your list (x):", min_value=1, value=24)
st.write("This is the number of items in the sample that are classified as 'successes' (e.g., synaptic proteins in your list).")

# Calculate the p-value
if st.button("Calculate P-value"):
    p_value = hypergeom.sf(x-1, M, n, N)
    st.write(f"**P-value:** {p_value}")
    st.write("The p-value represents the probability of obtaining at least the observed number of 'successes' in the sample.")

# Additional Information
st.header("About Hypergeometric Test")
st.write("""
The hypergeometric test is used to calculate the statistical significance of having a certain number of successes (e.g., specific genes or proteins) in a sample drawn from a population. 
It is commonly used in biology and other fields to determine whether the observed overlap between two sets is greater than would be expected by chance.
""")
