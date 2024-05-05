import tkinter
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
import pandas as pd
class DataAnalysis:    
    def mid2Summary(self, df : pd.DataFrame):
        # Step 1: For first 4 assignments
        assignments_df = df[['As:1', 'As:2', 'As:3', 'As:4']]
        assignments_stats = assignments_df.describe()
        assignments_stats.loc['iqr'] = assignments_stats.loc['75%'] - assignments_stats.loc['25%']
        assignments_stats.loc['std_dev'] = assignments_df.std()
        assignments_stats.loc['mean'] = assignments_df.mean()

        # Step 2: For first 4 quizzes
        quizzes_df = df[['Qz:1', 'Qz:2', 'Qz:3', 'Qz:4']]
        quizzes_stats = quizzes_df.describe()
        quizzes_stats.loc['iqr'] = quizzes_stats.loc['75%'] - quizzes_stats.loc['25%']
        quizzes_stats.loc['std_dev'] = quizzes_df.std()
        quizzes_stats.loc['mean'] = quizzes_df.mean()

        # Step 3: For S-1
        s_i_df = df['S-I']
        s_i_stats = s_i_df.describe()
        s_i_stats['iqr'] = s_i_stats['75%'] - s_i_stats['25%']
        s_i_stats['std_dev'] = s_i_df.std()
        s_i_stats['mean'] = s_i_df.mean()

        return {
            'Assignments Stats': assignments_stats,
            'Quizzes Stats': quizzes_stats,
            'S-1 Stats': s_i_stats
        }

    def finalsSummary(self, df : pd.DataFrame):
        # Step 1: For top 5 assignments
        assignments_df = df[['As']]
        assignments_stats = assignments_df.describe()
        assignments_stats.loc['iqr'] = assignments_stats.loc['75%'] - assignments_stats.loc['25%']
        assignments_stats.loc['std_dev'] = assignments_df.std()
        assignments_stats.loc['mean'] = assignments_df.mean()

        # Step 2: For top 5 quizzes
        quizzes_df = df[['Qz']]
        quizzes_stats = quizzes_df.describe()
        quizzes_stats.loc['iqr'] = quizzes_stats.loc['75%'] - quizzes_stats.loc['25%']
        quizzes_stats.loc['std_dev'] = quizzes_df.std()
        quizzes_stats.loc['mean'] = quizzes_df.mean()

        # Step 3: For S-1
        s_i_df = df['S-I']
        s_i_stats = s_i_df.describe()
        s_i_stats['iqr'] = s_i_stats['75%'] - s_i_stats['25%']
        s_i_stats['std_dev'] = s_i_df.std()
        s_i_stats['mean'] = s_i_df.mean()

        # Step 4: For S-2
        s_ii_df = df['S-II']
        s_ii_stats = s_ii_df.describe()
        s_ii_stats['iqr'] = s_ii_stats['75%'] - s_ii_stats['25%']
        s_ii_stats['std_dev'] = s_ii_df.std()
        s_ii_stats['mean'] = s_ii_df.mean()


        return {
            'Assignments Stats': assignments_stats,
            'Quizzes Stats': quizzes_stats,
            'S-1 Stats': s_i_stats,
            'S-2 Stats': s_ii_stats
        }

    def print_stats(self, stats):
        for key in stats:
            print(key)
            print(stats[key])
            print()

    # EDA before mid-2
    def EDA_Mid2(self, df : pd.DataFrame):
        
        # Create a figure and subplots
        fig, axs = plt.subplots(1, 3, figsize=(15, 5))

        # Boxplot for Assignments
        assignments = ['As:1', 'As:2', 'As:3', 'As:4']
        df.boxplot(column=assignments, ax=axs[0])
        axs[0].set_title('Boxplot of First 4 Assignments')

        # Boxplot for Quizzes
        quizzes = ['Qz:1', 'Qz:2', 'Qz:3', 'Qz:4']
        df.boxplot(column=quizzes, ax=axs[1])
        axs[1].set_title('Boxplot of First 4 Quizzes')

        # Boxplot for S-I
        df.boxplot(column=['S-I'], ax=axs[2])
        axs[2].set_title('Boxplot of S-I Marks')

        # Adjust layout
        plt.tight_layout()
        plt.show()

        # Assign colors based on grades
        colors = {'Pass': 'green', 'Fail': 'red'}

        # Calculate the sum of the first 4 assignments and first 4 quizzes
        df['Sum_Assignments'] = df[['As:1', 'As:2', 'As:3', 'As:4']].sum(axis=1)
        df['Sum_Quizzes'] = df[['Qz:1', 'Qz:2', 'Qz:3', 'Qz:4']].sum(axis=1)

        # Assign colors based on grades
        colors = {'Pass': 'green', 'Fail': 'red'}

        # Create a figure and subplots
        fig, axs = plt.subplots(1, 3, figsize=(15, 5))

        # Plot scatter plot for Sum of First 4 Assignments vs Sum of First 4 Quizzes
        axs[0].set_title('Sum of First 4 Assignments vs Sum of First 4 Quizzes')
        for grade, color in colors.items():
            axs[0].scatter(df[df['Grade'] == grade]['Sum_Assignments'], df[df['Grade'] == grade]['Sum_Quizzes'], c=color, label=grade)
        axs[0].set_xlabel('Sum of First 4 Assignments')
        axs[0].set_ylabel('Sum of First 4 Quizzes')
        axs[0].legend()
        axs[0].grid(True)

        # Plot scatter plot for Sum of First 4 Quizzes vs S-I Marks
        axs[1].set_title('Sum of First 4 Quizzes vs S-I Marks')
        for grade, color in colors.items():
            axs[1].scatter(df[df['Grade'] == grade]['Sum_Quizzes'], df[df['Grade'] == grade]['S-I'], c=color, label=grade)
        axs[1].set_xlabel('Sum of First 4 Quizzes')
        axs[1].set_ylabel('S-I Marks')
        axs[1].legend()
        axs[1].grid(True)

        # Plot scatter plot for Sum of First 4 Assignments vs S-I Marks
        axs[2].set_title('Sum of First 4 Assignments vs S-I Marks')
        for grade, color in colors.items():
            axs[2].scatter(df[df['Grade'] == grade]['Sum_Assignments'], df[df['Grade'] == grade]['S-I'], c=color, label=grade)
        axs[2].set_xlabel('Sum of First 4 Assignments')
        axs[2].set_ylabel('S-I Marks')
        axs[2].legend()
        axs[2].grid(True)

        # Adjust layout
        plt.tight_layout()
        plt.show()


    def EDA_Finals(self, df : pd.DataFrame):
        # Create a figure and subplots
        fig, axs = plt.subplots(2, 2, figsize=(12, 10))

        # Boxplot for As
        df.boxplot(column=['As'], ax=axs[0, 0])
        axs[0, 0].set_title('Boxplot of Sum of Top 5 Assignments')

        # Boxplot for Qz
        df.boxplot(column=['Qz'], ax=axs[0, 1])
        axs[0, 1].set_title('Boxplot of Sum of Top 5 Quizzes')

        # Boxplot for S-I
        df.boxplot(column=['S-I'], ax=axs[1, 0])
        axs[1, 0].set_title('Boxplot of S-1 Marks')

        # Boxplot for S-II
        df.boxplot(column=['S-II'], ax=axs[1, 1])
        axs[1, 1].set_title('Boxplot of S-2 Marks')

        # Adjust layout
        plt.tight_layout()
        plt.show()

        # Assign colors based on grades
        colors = {'Pass': 'green', 'Fail': 'red'}

        # Create subplots for each scatter plot
        fig, axs = plt.subplots(2, 3, figsize=(15, 10))


        # Scatter plot for As and Qz
        for grade, color in colors.items():
            axs[0, 0].scatter(df[df['Grade'] == grade]['As'], df[df['Grade'] == grade]['Qz'], c=color, label=grade)
        axs[0, 0].set_title('As vs Qz')
        axs[0, 0].set_xlabel('As')
        axs[0, 0].set_ylabel('Qz')
        axs[0, 0].legend()

        # Scatter plot for As and S-I
        for grade, color in colors.items():
            axs[0, 1].scatter(df[df['Grade'] == grade]['As'], df[df['Grade'] == grade]['S-I'], c=color, label=grade)
        axs[0, 1].set_title('As vs S-I')
        axs[0, 1].set_xlabel('As')
        axs[0, 1].set_ylabel('S-I')
        axs[0, 1].legend()

        # Scatter plot for As and S-II
        for grade, color in colors.items():
            axs[0, 2].scatter(df[df['Grade'] == grade]['As'], df[df['Grade'] == grade]['S-II'], c=color, label=grade)
        axs[0, 2].set_title('As vs S-II')
        axs[0, 2].set_xlabel('As')
        axs[0, 2].set_ylabel('S-II')
        axs[0, 2].legend()

        # Scatter plot for Qz and S-I
        for grade, color in colors.items():
            axs[1, 0].scatter(df[df['Grade'] == grade]['Qz'], df[df['Grade'] == grade]['S-I'], c=color, label=grade)
        axs[1, 0].set_title('Qz vs S-I')
        axs[1, 0].set_xlabel('Qz')
        axs[1, 0].set_ylabel('S-I')
        axs[1, 0].legend()

        # Scatter plot for Qz and S-II
        for grade, color in colors.items():
            axs[1, 1].scatter(df[df['Grade'] == grade]['Qz'], df[df['Grade'] == grade]['S-II'], c=color, label=grade)
        axs[1, 1].set_title('Qz vs S-II')
        axs[1, 1].set_xlabel('Qz')
        axs[1, 1].set_ylabel('S-II')
        axs[1, 1].legend()

        # Scatter plot for S-I and S-II
        for grade, color in colors.items():
            axs[1, 2].scatter(df[df['Grade'] == grade]['S-I'], df[df['Grade'] == grade]['S-II'], c=color, label=grade)
        axs[1, 2].set_title('S-I vs S-II')
        axs[1, 2].set_xlabel('S-I')
        axs[1, 2].set_ylabel('S-II')
        axs[1, 2].legend()

        # Adjust layout
        plt.tight_layout()
        plt.show()
