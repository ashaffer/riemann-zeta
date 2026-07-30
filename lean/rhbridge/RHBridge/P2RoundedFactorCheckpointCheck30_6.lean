import RHBridge.P2RoundedFactorCheckpointData30

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FactorChunk6 :
    P2RoundedFactorCheckpointData.panel30Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨30, by decide⟩ := by
  decide +kernel

theorem panel30Prefix24_eq :
    P2RoundedFactorCheckpointData.panel30Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk6.1

theorem panel30Prefix25_eq :
    P2RoundedFactorCheckpointData.panel30Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk6.2.1

theorem panel30Prefix26_eq :
    P2RoundedFactorCheckpointData.panel30Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk6.2.2.1

theorem panel30Prefix27_eq :
    P2RoundedFactorCheckpointData.panel30Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk6.2.2.2

end RHP2Bridge
