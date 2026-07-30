import RHBridge.P2RoundedFactorCheckpointData14

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FactorChunk9 :
    P2RoundedFactorCheckpointData.panel14Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨14, by decide⟩ := by
  decide +kernel

theorem panel14Prefix36_eq :
    P2RoundedFactorCheckpointData.panel14Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk9.1

theorem panel14Prefix37_eq :
    P2RoundedFactorCheckpointData.panel14Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk9.2.1

theorem panel14Prefix38_eq :
    P2RoundedFactorCheckpointData.panel14Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk9.2.2.1

theorem panel14Prefix39_eq :
    P2RoundedFactorCheckpointData.panel14Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk9.2.2.2

end RHP2Bridge
