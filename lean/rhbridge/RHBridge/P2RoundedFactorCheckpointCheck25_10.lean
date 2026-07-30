import RHBridge.P2RoundedFactorCheckpointData25

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FactorChunk10 :
    P2RoundedFactorCheckpointData.panel25Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨25, by decide⟩ := by
  decide +kernel

theorem panel25Prefix40_eq :
    P2RoundedFactorCheckpointData.panel25Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk10.1

theorem panel25Prefix41_eq :
    P2RoundedFactorCheckpointData.panel25Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk10.2.1

theorem panel25Prefix42_eq :
    P2RoundedFactorCheckpointData.panel25Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk10.2.2.1

theorem panel25Prefix43_eq :
    P2RoundedFactorCheckpointData.panel25Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk10.2.2.2

end RHP2Bridge
