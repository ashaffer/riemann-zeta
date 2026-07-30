import RHBridge.P2RoundedFactorCheckpointData3

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FactorChunk14 :
    P2RoundedFactorCheckpointData.panel3Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨3, by decide⟩ := by
  decide +kernel

theorem panel3Prefix56_eq :
    P2RoundedFactorCheckpointData.panel3Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk14.1

theorem panel3Prefix57_eq :
    P2RoundedFactorCheckpointData.panel3Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk14.2.1

theorem panel3Prefix58_eq :
    P2RoundedFactorCheckpointData.panel3Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk14.2.2.1

theorem panel3Prefix59_eq :
    P2RoundedFactorCheckpointData.panel3Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk14.2.2.2

end RHP2Bridge
