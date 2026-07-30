import RHBridge.P2RoundedFactorCheckpointData20

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FactorChunk7 :
    P2RoundedFactorCheckpointData.panel20Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨20, by decide⟩ := by
  decide +kernel

theorem panel20Prefix28_eq :
    P2RoundedFactorCheckpointData.panel20Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk7.1

theorem panel20Prefix29_eq :
    P2RoundedFactorCheckpointData.panel20Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk7.2.1

theorem panel20Prefix30_eq :
    P2RoundedFactorCheckpointData.panel20Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk7.2.2.1

theorem panel20Prefix31_eq :
    P2RoundedFactorCheckpointData.panel20Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk7.2.2.2

end RHP2Bridge
