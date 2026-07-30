import RHBridge.P2RoundedFactorCheckpointData10

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FactorChunk9 :
    P2RoundedFactorCheckpointData.panel10Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨10, by decide⟩ := by
  decide +kernel

theorem panel10Prefix36_eq :
    P2RoundedFactorCheckpointData.panel10Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk9.1

theorem panel10Prefix37_eq :
    P2RoundedFactorCheckpointData.panel10Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk9.2.1

theorem panel10Prefix38_eq :
    P2RoundedFactorCheckpointData.panel10Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk9.2.2.1

theorem panel10Prefix39_eq :
    P2RoundedFactorCheckpointData.panel10Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk9.2.2.2

end RHP2Bridge
