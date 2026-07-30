import RHBridge.P2RoundedFactorCheckpointData24

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FactorChunk9 :
    P2RoundedFactorCheckpointData.panel24Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨24, by decide⟩ := by
  decide +kernel

theorem panel24Prefix36_eq :
    P2RoundedFactorCheckpointData.panel24Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk9.1

theorem panel24Prefix37_eq :
    P2RoundedFactorCheckpointData.panel24Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk9.2.1

theorem panel24Prefix38_eq :
    P2RoundedFactorCheckpointData.panel24Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk9.2.2.1

theorem panel24Prefix39_eq :
    P2RoundedFactorCheckpointData.panel24Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk9.2.2.2

end RHP2Bridge
