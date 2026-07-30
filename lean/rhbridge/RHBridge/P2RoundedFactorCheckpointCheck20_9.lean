import RHBridge.P2RoundedFactorCheckpointData20

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FactorChunk9 :
    P2RoundedFactorCheckpointData.panel20Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨20, by decide⟩ := by
  decide +kernel

theorem panel20Prefix36_eq :
    P2RoundedFactorCheckpointData.panel20Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk9.1

theorem panel20Prefix37_eq :
    P2RoundedFactorCheckpointData.panel20Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk9.2.1

theorem panel20Prefix38_eq :
    P2RoundedFactorCheckpointData.panel20Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk9.2.2.1

theorem panel20Prefix39_eq :
    P2RoundedFactorCheckpointData.panel20Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk9.2.2.2

end RHP2Bridge
