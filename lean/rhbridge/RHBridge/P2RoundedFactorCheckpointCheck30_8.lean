import RHBridge.P2RoundedFactorCheckpointData30

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FactorChunk8 :
    P2RoundedFactorCheckpointData.panel30Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨30, by decide⟩ := by
  decide +kernel

theorem panel30Prefix32_eq :
    P2RoundedFactorCheckpointData.panel30Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk8.1

theorem panel30Prefix33_eq :
    P2RoundedFactorCheckpointData.panel30Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk8.2.1

theorem panel30Prefix34_eq :
    P2RoundedFactorCheckpointData.panel30Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk8.2.2.1

theorem panel30Prefix35_eq :
    P2RoundedFactorCheckpointData.panel30Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk8.2.2.2

end RHP2Bridge
