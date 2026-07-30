import RHBridge.P2RoundedFactorCheckpointData21

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FactorChunk9 :
    P2RoundedFactorCheckpointData.panel21Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨21, by decide⟩ := by
  decide +kernel

theorem panel21Prefix36_eq :
    P2RoundedFactorCheckpointData.panel21Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk9.1

theorem panel21Prefix37_eq :
    P2RoundedFactorCheckpointData.panel21Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk9.2.1

theorem panel21Prefix38_eq :
    P2RoundedFactorCheckpointData.panel21Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk9.2.2.1

theorem panel21Prefix39_eq :
    P2RoundedFactorCheckpointData.panel21Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk9.2.2.2

end RHP2Bridge
