import RHBridge.P2RoundedFactorCheckpointData8

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FactorChunk9 :
    P2RoundedFactorCheckpointData.panel8Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨8, by decide⟩ := by
  decide +kernel

theorem panel8Prefix36_eq :
    P2RoundedFactorCheckpointData.panel8Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk9.1

theorem panel8Prefix37_eq :
    P2RoundedFactorCheckpointData.panel8Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk9.2.1

theorem panel8Prefix38_eq :
    P2RoundedFactorCheckpointData.panel8Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk9.2.2.1

theorem panel8Prefix39_eq :
    P2RoundedFactorCheckpointData.panel8Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk9.2.2.2

end RHP2Bridge
