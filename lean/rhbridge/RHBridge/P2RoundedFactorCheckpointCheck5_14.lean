import RHBridge.P2RoundedFactorCheckpointData5

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FactorChunk14 :
    P2RoundedFactorCheckpointData.panel5Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨5, by decide⟩ := by
  decide +kernel

theorem panel5Prefix56_eq :
    P2RoundedFactorCheckpointData.panel5Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk14.1

theorem panel5Prefix57_eq :
    P2RoundedFactorCheckpointData.panel5Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk14.2.1

theorem panel5Prefix58_eq :
    P2RoundedFactorCheckpointData.panel5Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk14.2.2.1

theorem panel5Prefix59_eq :
    P2RoundedFactorCheckpointData.panel5Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk14.2.2.2

end RHP2Bridge
