import RHBridge.P2RoundedFactorCheckpointData20

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FactorChunk10 :
    P2RoundedFactorCheckpointData.panel20Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨20, by decide⟩ := by
  decide +kernel

theorem panel20Prefix40_eq :
    P2RoundedFactorCheckpointData.panel20Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk10.1

theorem panel20Prefix41_eq :
    P2RoundedFactorCheckpointData.panel20Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk10.2.1

theorem panel20Prefix42_eq :
    P2RoundedFactorCheckpointData.panel20Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk10.2.2.1

theorem panel20Prefix43_eq :
    P2RoundedFactorCheckpointData.panel20Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk10.2.2.2

end RHP2Bridge
