import RHBridge.P2RoundedFactorCheckpointData18

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FactorChunk9 :
    P2RoundedFactorCheckpointData.panel18Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨18, by decide⟩ := by
  decide +kernel

theorem panel18Prefix36_eq :
    P2RoundedFactorCheckpointData.panel18Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk9.1

theorem panel18Prefix37_eq :
    P2RoundedFactorCheckpointData.panel18Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk9.2.1

theorem panel18Prefix38_eq :
    P2RoundedFactorCheckpointData.panel18Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk9.2.2.1

theorem panel18Prefix39_eq :
    P2RoundedFactorCheckpointData.panel18Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk9.2.2.2

end RHP2Bridge
