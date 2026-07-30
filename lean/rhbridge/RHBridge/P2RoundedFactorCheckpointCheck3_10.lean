import RHBridge.P2RoundedFactorCheckpointData3

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FactorChunk10 :
    P2RoundedFactorCheckpointData.panel3Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨3, by decide⟩ := by
  decide +kernel

theorem panel3Prefix40_eq :
    P2RoundedFactorCheckpointData.panel3Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk10.1

theorem panel3Prefix41_eq :
    P2RoundedFactorCheckpointData.panel3Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk10.2.1

theorem panel3Prefix42_eq :
    P2RoundedFactorCheckpointData.panel3Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk10.2.2.1

theorem panel3Prefix43_eq :
    P2RoundedFactorCheckpointData.panel3Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk10.2.2.2

end RHP2Bridge
