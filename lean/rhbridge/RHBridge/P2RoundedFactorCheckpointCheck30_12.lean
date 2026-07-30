import RHBridge.P2RoundedFactorCheckpointData30

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FactorChunk12 :
    P2RoundedFactorCheckpointData.panel30Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨30, by decide⟩ := by
  decide +kernel

theorem panel30Prefix48_eq :
    P2RoundedFactorCheckpointData.panel30Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk12.1

theorem panel30Prefix49_eq :
    P2RoundedFactorCheckpointData.panel30Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk12.2.1

theorem panel30Prefix50_eq :
    P2RoundedFactorCheckpointData.panel30Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk12.2.2.1

theorem panel30Prefix51_eq :
    P2RoundedFactorCheckpointData.panel30Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk12.2.2.2

end RHP2Bridge
