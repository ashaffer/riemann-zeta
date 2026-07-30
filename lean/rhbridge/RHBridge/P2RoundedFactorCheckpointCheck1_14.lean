import RHBridge.P2RoundedFactorCheckpointData1

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FactorChunk14 :
    P2RoundedFactorCheckpointData.panel1Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨1, by decide⟩ := by
  decide +kernel

theorem panel1Prefix56_eq :
    P2RoundedFactorCheckpointData.panel1Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk14.1

theorem panel1Prefix57_eq :
    P2RoundedFactorCheckpointData.panel1Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk14.2.1

theorem panel1Prefix58_eq :
    P2RoundedFactorCheckpointData.panel1Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk14.2.2.1

theorem panel1Prefix59_eq :
    P2RoundedFactorCheckpointData.panel1Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk14.2.2.2

end RHP2Bridge
