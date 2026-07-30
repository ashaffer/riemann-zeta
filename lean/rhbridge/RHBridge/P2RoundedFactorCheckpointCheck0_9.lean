import RHBridge.P2RoundedFactorCheckpointData0

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FactorChunk9 :
    P2RoundedFactorCheckpointData.panel0Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨0, by decide⟩ := by
  decide +kernel

theorem panel0Prefix36_eq :
    P2RoundedFactorCheckpointData.panel0Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk9.1

theorem panel0Prefix37_eq :
    P2RoundedFactorCheckpointData.panel0Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk9.2.1

theorem panel0Prefix38_eq :
    P2RoundedFactorCheckpointData.panel0Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk9.2.2.1

theorem panel0Prefix39_eq :
    P2RoundedFactorCheckpointData.panel0Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk9.2.2.2

end RHP2Bridge
