import RHBridge.P2RoundedFactorCheckpointData31

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FactorChunk9 :
    P2RoundedFactorCheckpointData.panel31Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨31, by decide⟩ := by
  decide +kernel

theorem panel31Prefix36_eq :
    P2RoundedFactorCheckpointData.panel31Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk9.1

theorem panel31Prefix37_eq :
    P2RoundedFactorCheckpointData.panel31Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk9.2.1

theorem panel31Prefix38_eq :
    P2RoundedFactorCheckpointData.panel31Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk9.2.2.1

theorem panel31Prefix39_eq :
    P2RoundedFactorCheckpointData.panel31Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk9.2.2.2

end RHP2Bridge
