import RHBridge.P2RoundedFactorCheckpointData20

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FactorChunk0 :
    P2RoundedFactorCheckpointData.panel20Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨20, by decide⟩ := by
  decide +kernel

theorem panel20Prefix0_eq :
    P2RoundedFactorCheckpointData.panel20Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk0.1

theorem panel20Prefix1_eq :
    P2RoundedFactorCheckpointData.panel20Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk0.2.1

theorem panel20Prefix2_eq :
    P2RoundedFactorCheckpointData.panel20Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk0.2.2.1

theorem panel20Prefix3_eq :
    P2RoundedFactorCheckpointData.panel20Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk0.2.2.2

end RHP2Bridge
