import RHBridge.P2RoundedFactorCheckpointData8

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FactorChunk6 :
    P2RoundedFactorCheckpointData.panel8Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨8, by decide⟩ := by
  decide +kernel

theorem panel8Prefix24_eq :
    P2RoundedFactorCheckpointData.panel8Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk6.1

theorem panel8Prefix25_eq :
    P2RoundedFactorCheckpointData.panel8Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk6.2.1

theorem panel8Prefix26_eq :
    P2RoundedFactorCheckpointData.panel8Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk6.2.2.1

theorem panel8Prefix27_eq :
    P2RoundedFactorCheckpointData.panel8Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk6.2.2.2

end RHP2Bridge
