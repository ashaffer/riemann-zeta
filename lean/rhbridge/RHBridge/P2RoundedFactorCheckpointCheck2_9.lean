import RHBridge.P2RoundedFactorCheckpointData2

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FactorChunk9 :
    P2RoundedFactorCheckpointData.panel2Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨2, by decide⟩ := by
  decide +kernel

theorem panel2Prefix36_eq :
    P2RoundedFactorCheckpointData.panel2Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk9.1

theorem panel2Prefix37_eq :
    P2RoundedFactorCheckpointData.panel2Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk9.2.1

theorem panel2Prefix38_eq :
    P2RoundedFactorCheckpointData.panel2Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk9.2.2.1

theorem panel2Prefix39_eq :
    P2RoundedFactorCheckpointData.panel2Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk9.2.2.2

end RHP2Bridge
