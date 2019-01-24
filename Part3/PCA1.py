# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 20:17:03 2018

@author: KoalaChelsea
"""

#%%
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
# =============================================================================
# 
# =============================================================================

def main():
    ## Read this data using pandas as a dataframe.
    data = pd.read_csv("C:/Users/chels/OneDrive/Documents/ANLY501/Project/Part2/RawData/Full_Information_Cleaned.csv")
    print(data.columns)
    
    ## Identify the features
    #internal = ['category_x', 'Accept_Credit_Card', 'Alcohol', 
    #            'Outdoor_Seating', 'Parking', 'Take_out', 'Takes_Reservations', 
    #            'WIFI', 'Ambience', 'Attire', 'Noise_Level', 'average_price']
    internal = ['Accept_Credit_Card', 'Outdoor_Seating', 'Take_out', 
                'Takes_Reservations', 'WIFI', 'Noise_Level','average_price']
    external = ['atm', 'bank', 'bar','beauty_salon', 'bus_station', 'cafe', 
                'gym', 'school']
    demography = ['White population', 'Black population', 
                  'American Indian population', 'Asian population', 
                  'Hispanic or Latino population', 'High school or higher', 
                  'Graduate or professional degree', 'Unemployed']

    ###########################################################################
    ## PCA for internal
    
    ## Separating out the features
    internal_x = data.loc[:, internal].values
    
    ## Standardize the Data
    internal_x = StandardScaler().fit_transform(internal_x)
    
    ## PCA Projection to 2D
    pca_internal = PCA(n_components=2)
    internal_x_pca = pca_internal.fit_transform(internal_x)
    print("original shape:   ", internal_x.shape)
    print("transformed shape:", internal_x_pca.shape)
    
    principalDf_internal = pd.DataFrame(data = internal_x_pca, 
                               columns = ['principal component 1', 
                                          'principal component 2'])
    print("explained_variance_ratio_", pca_internal.explained_variance_ratio_)
    
    #######################################
    ## review count
    internal_finalDf_review = pd.concat([principalDf_internal, 
                                data['review_count_binned']], 
                               axis = 1)
    print("Internal finalDf for review shape:", internal_finalDf_review.shape)

    ## Visualize 2D Projection
    fig = plt.figure(figsize = (8,8))
    ax = fig.add_subplot(1,1,1)
    ax.set_xlabel('Principal Component 1', fontsize = 12)
    ax.set_ylabel('Principal Component 2', fontsize = 12)
    ax.set_title('2 component internal PCA for review_count', fontsize = 20)
    
    review = ['Small No Review','Medium No Reviews','Meadium to Large Reviews'
              ,'large Number of Reviews', 'Very Popular Resturant']
    colors = ['blue','green','yellow','orange','red']
    for review, color in zip(review,colors):
        indicesToKeep = internal_finalDf_review['review_count_binned'] == review
        ax.scatter(internal_finalDf_review.loc[indicesToKeep, 'principal component 1']
                   , internal_finalDf_review.loc[indicesToKeep, 'principal component 2']
                   , c = color, alpha=0.5, s = 30)
    ax.legend(review, loc='best', 
              labels = ('Small No Review','Medium No Reviews',
                                'Meadium to Large Reviews',
                                'large Number of Reviews', 
                                'Very Popular Resturant'))
    ax.grid()
    plt.show()
    plt.close()
    
    
    #######################################
    ## rating
    internal_finalDf_rating = pd.concat([principalDf_internal, data['rating']], 
                               axis = 1)
    print("External finalDf for rating shape:", internal_finalDf_rating.shape)
    
    ## Visualize 2D Projection
    fig = plt.figure(figsize = (8,8))
    ax = fig.add_subplot(1,1,1)
    ax.set_xlabel('Principal Component 1', fontsize = 12)
    ax.set_ylabel('Principal Component 2', fontsize = 12)
    ax.set_title('2 component internal PCA for rating', fontsize = 20)
    
    rating = [1, 1.5, 2.0,2.5,3.0,3.5,4.0,4.5,5.0]
    colors = ['#191970','#0000cd','#00bfff','#add8e6','#f0e68c', '#ffd700', 
              '#ff8c00', '#ff4500', '#b22222']
    for rating, color in zip(rating, colors):
        indicesToKeep = internal_finalDf_rating['rating'] == rating
        ax.scatter(internal_finalDf_rating.loc[indicesToKeep, 'principal component 1']
                   , internal_finalDf_rating.loc[indicesToKeep, 'principal component 2']
                   , c = color, alpha=0.5, s = 30)
    ax.legend(rating, loc='best', 
              labels = ('1', '1.5', '2','2.5','3','3.5','4','4.5','5'))
    ax.grid()
    plt.show()
    plt.close()
    
    
    ###########################################################################
    ## PCA for external
    
    ## Separating out the features
    external_x = data.loc[:, external].values
    
    ## Standardize the Data
    external_x = StandardScaler().fit_transform(external_x)
    
    ## PCA Projection to 2D
    pca_external = PCA(n_components=2)
    external_x_pca = pca_external.fit_transform(external_x)
    print("original shape:   ", external_x.shape)
    print("transformed shape:", external_x_pca.shape)
    
    principalDf_external = pd.DataFrame(data = external_x_pca, 
                               columns = ['principal component 1', 
                                          'principal component 2'])
    print("explained_variance_ratio_", pca_external.explained_variance_ratio_)
    
    #######################################
    ## review count
    external_finalDf_review = pd.concat([principalDf_external, 
                                data['review_count_binned']], 
                               axis = 1)
    print("External finalDf for review shape:", external_finalDf_review.shape)

    ## Visualize 2D Projection
    fig = plt.figure(figsize = (8,8))
    ax = fig.add_subplot(1,1,1)
    ax.set_xlabel('Principal Component 1', fontsize = 12)
    ax.set_ylabel('Principal Component 2', fontsize = 12)
    ax.set_title('2 component external PCA for review_count', fontsize = 20)
    
    review = ['Small No Review','Medium No Reviews','Meadium to Large Reviews'
              ,'large Number of Reviews', 'Very Popular Resturant']
    colors = ['blue','green','yellow','orange','red']
    for review, color in zip(review,colors):
        indicesToKeep = external_finalDf_review['review_count_binned'] == review
        ax.scatter(external_finalDf_review.loc[indicesToKeep, 'principal component 1']
                   , external_finalDf_review.loc[indicesToKeep, 'principal component 2']
                   , c = color, alpha=0.5, s = 30)
    ax.legend(review, loc='best', 
              labels = ('Small No Review','Medium No Reviews',
                                'Meadium to Large Reviews',
                                'large Number of Reviews', 
                                'Very Popular Resturant'))
    ax.grid()
    plt.show()
    plt.close()
    
    #######################################
    ## rating
    external_finalDf_rating = pd.concat([principalDf_external, data['rating']], 
                               axis = 1)
    print("External finalDf for rating shape:", external_finalDf_rating.shape)
    
    ## Visualize 2D Projection
    fig = plt.figure(figsize = (8,8))
    ax = fig.add_subplot(1,1,1)
    ax.set_xlabel('Principal Component 1', fontsize = 12)
    ax.set_ylabel('Principal Component 2', fontsize = 12)
    ax.set_title('2 component external PCA for rating', fontsize = 20)
    
    rating = [1, 1.5, 2.0,2.5,3.0,3.5,4.0,4.5,5.0]
    colors = ['#191970','#0000cd','#00bfff','#add8e6','#f0e68c', '#ffd700', 
              '#ff8c00', '#ff4500', '#b22222']
    for rating, color in zip(rating, colors):
        indicesToKeep = external_finalDf_rating['rating'] == rating
        ax.scatter(external_finalDf_rating.loc[indicesToKeep, 'principal component 1']
                   , external_finalDf_rating.loc[indicesToKeep, 'principal component 2']
                   , c = color, alpha=0.5, s = 30)
    ax.legend(rating, loc='best', 
              labels = ('1', '1.5', '2','2.5','3','3.5','4','4.5','5'))
    ax.grid()
    plt.show()
    plt.close()
    
    
    ###########################################################################
    ## PCA for demography
    
    ## Separating out the features
    demography_x = data.loc[:, demography].values
    
    ## Standardize the Data
    demography_x = StandardScaler().fit_transform(demography_x)
    
    ## PCA Projection to 2D
    pca_demography = PCA(n_components=2)
    demography_x_pca = pca_demography.fit_transform(demography_x)
    print("original shape:   ", demography_x .shape)
    print("transformed shape:", demography_x_pca.shape)
    
    principalDf_demography = pd.DataFrame(data = demography_x_pca, 
                               columns = ['principal component 1', 
                                          'principal component 2'])
    
    print("explained_variance_ratio_", pca_demography.explained_variance_ratio_)
    
    
    #######################################
    ## review count
    demography_finalDf_review = pd.concat([principalDf_demography, 
                                data['review_count_binned']], 
                               axis = 1)
    print("Demography finalDf for review shape:", demography_finalDf_review.shape)

    ## Visualize 2D Projection
    fig = plt.figure(figsize = (8,8))
    ax = fig.add_subplot(1,1,1)
    ax.set_xlabel('Principal Component 1', fontsize = 12)
    ax.set_ylabel('Principal Component 2', fontsize = 12)
    ax.set_title('2 component demography PCA for review_count', fontsize = 20)
    
    review = ['Small No Review','Medium No Reviews','Meadium to Large Reviews'
              ,'large Number of Reviews', 'Very Popular Resturant']
    colors = ['blue','green','yellow','orange','red']
    for review, color in zip(review,colors):
        indicesToKeep = demography_finalDf_review['review_count_binned'] == review
        ax.scatter(demography_finalDf_review.loc[indicesToKeep, 'principal component 1']
                   , demography_finalDf_review.loc[indicesToKeep, 'principal component 2']
                   , c = color, alpha=0.5, s = 30)
    ax.legend(review, loc='best', 
              labels = ('Small No Review','Medium No Reviews',
                                'Meadium to Large Reviews',
                                'large Number of Reviews', 
                                'Very Popular Resturant'))
    ax.grid()
    plt.show()
    plt.close()
    
    #######################################
    ## rating
    demography_finalDf_rating = pd.concat([principalDf_demography, data['rating']], 
                               axis = 1)
    print("Demography finalDf for rating shape:", demography_finalDf_rating.shape)
    
    ## Visualize 2D Projection
    fig = plt.figure(figsize = (8,8))
    ax = fig.add_subplot(1,1,1)
    ax.set_xlabel('Principal Component 1', fontsize = 12)
    ax.set_ylabel('Principal Component 2', fontsize = 12)
    ax.set_title('2 component demography PCA for rating', fontsize = 20)
    
    rating = [1, 1.5, 2.0,2.5,3.0,3.5,4.0,4.5,5.0]
    colors = ['#191970','#0000cd','#00bfff','#add8e6','#f0e68c', '#ffd700', 
              '#ff8c00', '#ff4500', '#b22222']
    for rating, color in zip(rating, colors):
        indicesToKeep = demography_finalDf_rating['rating'] == rating
        ax.scatter(demography_finalDf_rating.loc[indicesToKeep, 'principal component 1']
                   , demography_finalDf_rating.loc[indicesToKeep, 'principal component 2']
                   , c = color, alpha=0.5, s = 30)
    ax.legend(rating, loc='best', 
              labels = ('1', '1.5', '2','2.5','3','3.5','4','4.5','5'))
    ax.grid()
    plt.show()
    plt.close()
    


if __name__ == "__main__":
	 main()
     

