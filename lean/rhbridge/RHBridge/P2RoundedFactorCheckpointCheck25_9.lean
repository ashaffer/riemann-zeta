import RHBridge.P2RoundedFactorCheckpointData25

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FactorChunk9 :
    P2RoundedFactorCheckpointData.panel25Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨25, by decide⟩ := by
  decide +kernel

theorem panel25Prefix36_eq :
    P2RoundedFactorCheckpointData.panel25Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk9.1

theorem panel25Prefix37_eq :
    P2RoundedFactorCheckpointData.panel25Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk9.2.1

theorem panel25Prefix38_eq :
    P2RoundedFactorCheckpointData.panel25Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk9.2.2.1

theorem panel25Prefix39_eq :
    P2RoundedFactorCheckpointData.panel25Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk9.2.2.2

end RHP2Bridge
